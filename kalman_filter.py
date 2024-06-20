import numpy as np


# Kalman filter initialization
angle_est = np.zeros(2)  # [roll, pitch]
bias = np.zeros(2)  # [roll_bias, pitch_bias]
P = np.array([[1, 0], [0, 1]]) * np.eye(2)
Q_angle = 0.01
Q_bias = 0.003
R_measure = 0.03
FS = 25
dt = 1/FS  # 25Hz sampling rate

def kalman_filter(acc_angle, gyro_rate, dt, angle_est_prev, bias_prev, P_prev, Q_angle, Q_bias, R_measure):
    """
    Perform a single step of the Kalman filter to fuse accelerometer and gyroscope data.

    :param acc_angle: Angle measured by the accelerometer (degrees)
    :param gyro_rate: Angular velocity measured by the gyroscope (degrees/sec)
    :param dt: Time interval (sec)
    :param angle_est_prev: Previous estimated angle (degrees)
    :param bias_prev: Previous estimated gyro bias
    :param P_prev: Previous error covariance matrix
    :param Q_angle: Process noise variance for the angle
    :param Q_bias: Process noise variance for the bias
    :param R_measure: Measurement noise variance
    :return: Updated angle estimate, bias estimate, and error covariance matrix
    """
    # Predict phase
    rate = gyro_rate - bias_prev
    angle_est = angle_est_prev + dt * rate

    # Update error covariance matrix
    P = P_prev + dt * np.array([[dt*P_prev[1][1], -dt*P_prev[1][1]],
                                [-dt*P_prev[1][1], Q_bias + dt*P_prev[1][1]]])

    # Measurement update
    innovation = acc_angle - angle_est
    S = P[0][0] + R_measure
    K = P[:, 0] / S

    # New estimates
    angle_est += K[0] * innovation
    bias_est = bias_prev + K[1] * innovation

    # Update error covariance matrix
    P = (np.eye(2) - K[:, None] * np.array([1, 0])) @ P

    return angle_est, bias_est, P




def compute_euler_angles_kalman(acc_data, gyro_data, dt):
    """
    Compute Euler angles (roll, pitch) using accelerometer data fused with gyroscope data through a Kalman filter.

    :param acc_data: List of tuples (acc_x, acc_y, acc_z) from accelerometer
    :param gyro_data: List of tuples (gyro_x, gyro_y, gyro_z) from gyroscope
    :param dt: Time interval between measurements
    :return: List of tuples (roll, pitch)
    """
    timeseries_length = acc_data.shape[0]
    # Each row will have [roll, pitch]
    euler_angles = np.zeros((timeseries_length, 2))

    # Kalman filter initialization
    angle_est = np.zeros(2)  # [roll, pitch]
    bias = np.zeros(2)  # [roll_bias, pitch_bias]
    P = np.array([[1, 0], [0, 1]]) * np.eye(2)
    Q_angle = 0.01
    Q_bias = 0.003
    R_measure = 0.03

    for time_step in range(timeseries_length):
        acc_x, acc_y, acc_z = acc_data[time_step, :]
        gyro_x, gyro_y, gyro_z = gyro_data[time_step, :]

        # Compute angles from accelerometer
        roll_acc = np.arctan2(acc_y, acc_z) * 180 / np.pi
        pitch_acc = np.arctan2(-acc_x, np.sqrt(acc_y ** 2 + acc_z**2)) * 180 / np.pi

        # Kalman filter for roll
        roll, roll_bias, P_roll = kalman_filter(
            roll_acc, gyro_x, dt, angle_est[0], bias[0], P, Q_angle, Q_bias, R_measure)
        angle_est[0], bias[0], P = roll, roll_bias, P_roll

        # Kalman filter for pitch
        pitch, pitch_bias, P_pitch = kalman_filter(
            pitch_acc, gyro_y, dt, angle_est[1], bias[1], P, Q_angle, Q_bias, R_measure)
        angle_est[1], bias[1], P = pitch, pitch_bias, P_pitch

        # Store results
        euler_angles[time_step, :] = [roll, pitch]

    return euler_angles