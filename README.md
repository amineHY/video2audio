# Desciption
This is a simple python project that take a youtube video/playlist URL and convert it to audio

# prerequisites
* From the base installation of python, install additionnal python packages
    ``` bash
    pip install -r ffmpeg-python youtube-dl
    ```

* You may also install `libav-tools` librairie
    ``` bash
    apt-get install -y libav-tools
    ```

# Run the python script

```bash
python video2audio.py
```
the audio files should be saved in a new created folder `audio`.

**Note**: You can edit the option of [youtube-dl](https://github.com/ytdl-org/youtube-dl) if you want.

