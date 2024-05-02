from moviepy.editor import VideoFileClip

# Load the video file
video_path = 'ConvertidoraGIF//videoGitIgnore.mp4'
video = VideoFileClip(video_path)

# Trim the complete duration of the video
# gif_clip = video.subclip(0, video.duration) <- este es el uso correcto, pero nuestro video no tiene "duracion" 

gif_clip = video.subclip(0, 25)

# Define the path to save the full duration GIF
gif_path = 'ConvertidoraGIF//videoGitIgnore.gif'

# Save the trimmed clip as a GIF for the full duration
gif_clip.write_gif(gif_path, fps=10)

# Output the path to the GIF file
gif_path