#MP4 to GIF Converter in PYTHON!

from moviepy import VideoFileClip, vfx

clip = VideoFileClip(r"C:\Users\Daniel\Music\video1.mp4").subclipped(27.5, 32.5).resized(width=480).with_effects([vfx.MultiplySpeed(4)])

clip.write_gif(r"C:\Users\Daniel\Music\output.gif")


#Parameters:
#subclipped(start point, end point) - Dividing Clip
#resized(width=480) - Resize Window of Clip
#with_effects([vfx.MultiplySpeed(4)]) - How many times the Normal Speed
