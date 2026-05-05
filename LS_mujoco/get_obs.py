import mujoco
import numpy as np

class GimbalSystem:
    def __init__(self, xml_path):
        self.model = mujoco.MjModel.from_xml_path(xml_path)
        self.data  = mujoco.MjData(self.model)

        self.joint_id = {
            "joint1": self.model.joint("joint1").id,
            "joint2": self.model.joint("joint2").id
        }
        self.actuator_id = {
            "m1": self.model.actuator("m1").id,
            "m2": self.model.actuator("m2").id
        }

        self.jointData = []

    def read_data(self):
        return {
            "joint1": [self.data.sensor("joint1_pos").data[0], self.data.sensor("joint1_vel").data[0]],
            "joint2": [self.data.sensor("joint2_pos").data[0], self.data.sensor("joint2_vel").data[0]],
        }
    
    def set_actuator(self, name, value):
        self.data.ctrl[self.actuator_id[name]] = value
    
