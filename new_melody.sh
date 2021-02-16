#!/usr/bin/env bash

if [ "$1" == "purge" ]
then
./play_midi.py --midi_dir melody_output --purge
fi

if [ "$1" == "play" ]
then
melody_rnn_generate \
--config=lookback_rnn \
--bundle_file=lookback_rnn.mag \
--output_dir=./melody_output \
--num_outputs=10 \
--num_steps=128 \
--primer_melody="[60]"

./play_midi.py --midi_dir melody_output --play
fi

