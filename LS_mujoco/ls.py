import mujoco
import mujoco.viewer
import time
from get_obs import GimbalSystem
import numpy as np
from vofa import VOFA

system = GimbalSystem("scence.xml")
vofa = VOFA()

dt = system.model.opt.timestep
t = 0.0

theta = np.zeros((4, 1))
P = np.eye(4) * 1000  # P

y_k1, y_k2 = 0.0, 0.0
u_k1, u_k2 = 0.0, 0.0

with mujoco.viewer.launch_passive(system.model, system.data) as viewer:
    while viewer.is_running():
        start = time.time()
        mujoco.mj_step(system.model, system.data)

        u = 0.3 * np.sin(2*np.pi*0.5*t) 
        # u = 0.3 if t >= 2 else 0.0
        system.set_actuator("m1", u)

        joint_data = system.read_data()
        y = joint_data["joint1"][0]

        vofa.send_command(u, y)
        # print(u, y)
        phi = np.array([[y_k1],
                    [y_k2],
                    [u_k1],
                    [u_k2]])

        K = P @ phi /  (1 + phi.T @ P @ phi)
        y_hat = phi.T @ theta
        e = y - y_hat

        theta = theta + K * e
        P = (np.eye(4) - K @ phi.T) @ P

        y_k2 = y_k1
        y_k1 = y
        u_k2 = u_k1
        u_k1 = u

        print(theta.flatten())


        t += dt

        viewer.sync()
        elapsed = time.time() - start
        if elapsed < dt:
            time.sleep(dt - elapsed)