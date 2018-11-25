# olp_smartwatch

## gesture
- link: localhost:5000/predict_gesture
- method: post
- data: list points of data, each point has yaw, pitch, roll, ax, ay, ax, timestamp
- number of data: about 30 point
- return: ['up', 'down', 'right', 'left']
## activity
- link: localhost:5000/predict_activity
- method: post
- data: list points of data, each point has yaw, pitch, roll, ax, ay, ax, timestamp
- number of data: sent in stream
- return: ['running', 'walking', 'standing']
