from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("sorting_algorithm_visualization/my_sorting_algorithm.mp4")

videoClip.write_gif("sorting_algorithm_visualization/my_sorting_algorithm.gif")

