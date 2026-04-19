from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
clip1 = VideoFileClip('1.mp4').subclip(10, 20).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip2 = VideoFileClip('2.mp4').subclip(10, 20).fx(vfx.colorx, 1.5)\
                                                .fx(vfx.lum_contrast, 0, 50, 128)
combined = concatenate_videoclips([clip1, clip2])
combined.write_videofile('Combined4.mp4')