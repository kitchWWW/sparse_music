#!/bin/bash
rm output_.midi
rm output_.pdf
rm out/output_.ly
python3 create.py

cd out

/Applications/LilyPond.app/Contents/Resources/bin/lilypond output_.ly
open output_.pdf
# timidity output_.midi
cd ..