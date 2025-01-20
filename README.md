# generate-sample-mp3

For creating stereo mp3 files.

## files

After execute commands those files are going to be generated under out/ folder.

- stereo_test.mp3
  1 sec silence
  1 sec 440Hz on left audio
  1 sec 440Hz on right audio
  repeat 30 sec

- stereo_volume_x.mp3
  same with stereo_test.mp3 but output volume is adjusted

## set-up project

```shell
$ mise install
$ rye sync
$ rye run dev
# or
$ rye run vol
```

![Screenshot](docs/img/audio_input.png)
