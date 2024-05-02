# import cv2

# def get_annotated_frames(video_path):
#     """
#     Extract frames from a video and annotate them (if needed).
    
#     Args:
#         video_path (str): Path to the video file.
    
#     Returns:
#         List of annotated frames.
#     """
  
#     return frames

# def gen_bounding_boxes(frame):
#     """
#     Extract bounding box coordinates or number from a frame.
    
#     Args:
#         frame: Input frame.
    
#     Returns:
#         Bounding box coordinates or number.
#     """
#     # Perform object detection to get bounding boxes
#     bounding_boxes = detect_objects(frame)
#     return len(bounding_boxes)

# def get_action(frame):
#     """
#     Identify actions or activities in a frame.
    
#     Args:
#         frame: Input frame.
    
#     Returns:
#         Action label.
#     """
#     # Perform action recognition on the frame
#     action = recognize_action(frame)
#     return action

# # Example utility functions (to be implemented)
# def annotate_frame(frame):
#     # Example annotation function
#     # (e.g., draw bounding boxes, labels, etc.)
#     pass

# def detect_objects(frame):
#     # Example object detection function
#     # (e.g., using a pre-trained object detection model)
#     pass

# def recognize_action(frame):
#     # Example action recognition function
#     # (e.g., using a pre-trained action recognition model)
#     pass

# def get_all_bounding_boxes_in_current_frame(bounding_box_annotations_and_frames)
#     #Gets all the boxes currently in this frame:
#     pass

# def compute_what_box_disappeared(frame,old_frame):
#     #Computes difference between frames.
#     pass

# def extract_single_player_trajectory(id_to_end,starting_frames,i):
#     #Clip a single player trajectory of one of the bounded boxes
#     pass

# def predict_player_in_frame(frame):
#     #Predict the player
#     pass

# def get_final_player_prediction(prediction_stats):
#     #Use Reasoning to predict the player stats, bounding box collision etc
#     pass

# def map_trajectory_to_player(final_prediction,trajectory):
#     #Map the player and trajectory to each other for scouting
#     pass

# def add_predicted_actions_that_happened_in_trajectory(trajectory):
#     #Predict what the player did in the sequence of frames and add to trajectory object
#     for frame in trajectory:
#         trajectory[frame]['action'] = get_action(frame)
#     pass
# def feed_trajectory_info_to_llm(trajectory):
#     #LLM gets data in some way
#     report = ['','','']
#     return report

# def store_result_of_trajectory(report,player_id):
#     #Checks reports and maybe compiles the various reports of this player in someway..
#     pass

# def get_trajectories(bounding_box_annotations_and_frames):
#     # Example Trajectory compute from annotations from sequential frames
#     trajectories = []
#     bounding_boxes_in_current_frame = []
#     bounding_boxes_in_current_frame = get_all_bounding_boxes_in_current_frame(bounding_box_annotations_and_frames)
#     starting_frames = [0]*bounding_boxes_in_current_frame
#     bounding_box_dissapear = False
#     old_frame = None
#     min_trajectory_length = 10
#     for i, frame in enumerate(bounding_box_annotations_and_frames):
#         if bounding_box_dissapear and old_frame != None:
#             id_to_end = compute_what_box_disappeared(frame,old_frame)
#             potential_trajectory = extract_single_player_trajectory(id_to_end,starting_frames,i,bounding_box_annotations_and_frames)
#             if len(potential_trajectory) > min_trajectory_length: 
#                 trajectories.append(potential_trajectory)

#         old_frame = frame

#     return trajectories

# def identify_player_and_map_trajectory_to_player(trajectory):
#     #Takes a trajectory, and guesses the player.
#     #Marks this trajectory as belonging to a certain player, for scouting purposes.
#     prediction_stats = []
#     trajectory = add_predicted_actions_that_happened_in_trajectory(trajectory) #dribble shoot, score etc...
#     for frame in trajectory:
#         prediction_stats.append(predict_player_in_frame(frame))


#     final_prediction = get_final_player_prediction(prediction_stats)
#     map_trajectory_to_player(final_prediction,trajectory)
#     return final_prediction
    

# def main():

#     video_path = "path/to/your/video.mp4"
#     # Step 1: Generate Bounding boxes annotations for each frame.
#     bounding_box_annotations_and_frames = gen_bounding_boxes(video_path)

#     # Step 2: Find continuous bounding box trajectories
#     trajectories = get_trajectories(bounding_box_annotations_and_frames)

#     # Step 3: Identify player in trajectory, for future mapping of scouting.
#     for trajectory in trajectories:
#         player_id = identify_player_and_map_trajectory_to_player(trajectory)
#         results = feed_trajectory_info_to_llm(trajectory)
#         store_result_of_trajectory(results,player_id)
    

