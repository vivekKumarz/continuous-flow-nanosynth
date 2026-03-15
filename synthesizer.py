import numpy as np
import time

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value):
        error = setpoint - measured_value
        self.integral += error
        derivative = error - self.prev_error
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        self.prev_error = error
        return output

class NanoparticleSurrogateModel:
    def predict_size(self, temp, flow_rate):
        # Mocking a Neural Network surrogate model trained on synthesis data
        return 5 + (temp * 0.1) - (flow_rate * 2) + np.random.normal(0, 0.1)

class ClosedLoopSynthesizer:
    """
    Closed-loop control of nanoparticle synthesis using a surrogate ML model
    and a PID controller for precision flow-rate adjustments.
    """
    def __init__(self):
        self.model = NanoparticleSurrogateModel()
        self.pid = PIDController(kp=0.5, ki=0.1, kd=0.05)

    def run_synthesis(self, target_nm: float):
        current_temp = 95.0
        current_flow = 1.0
        print(f"--- Starting Closed-Loop Synthesis for {target_nm} nm ---")
        
        for _ in range(10):
            predicted_size = self.model.predict_size(current_temp, current_flow)
            adjustment = self.pid.compute(target_nm, predicted_size)
            current_flow += adjustment
            print(f"Measured: {predicted_size:.2f} nm | Adjusting flow to: {current_flow:.4f} ml/min")
            time.sleep(0.2)

if __name__ == "__main__":
    synth = ClosedLoopSynthesizer()
    synth.run_synthesis(target_nm=12.5)
