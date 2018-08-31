\version "2.18.2"
		
#(set-default-paper-size "letter" 'landscape)
#(set-global-staff-size 24)


\header{
title ="Slow Music"
subtitle="
"

composer = "Brian Ellis"
tagline =""
}
\score{
\midi {}
\layout{}


<<

	
\new Staff \with {
  instrumentName = #"Solo"
  shortInstrumentName = #""
  midiInstrument = "French Horn"
}{
	\absolute{
\override Staff.TimeSignature.stencil = ##f

s4. d''4 \(c''8\) s4 
 s4. g'4 \(f'8\) s4 
 s4. f'4 \(g'8\) s4 
 s2 g'4 \( a'4 
   ~ a'4   c''4 bes'8\) s2 s8 
   \break  s2 e'4 s4 
 s4. a'8 \(g'4\) s4 
 s8 s2 b'8 \( c''4 
 a'8 bes'4\) s2 s8 
 s4. a'4 \(aes'4\) s8 
 c'1 s4 
	}

}	

\new StaffGroup <<
\new Staff \with {
  instrumentName = #""
  shortInstrumentName = #""
  midiInstrument = "Violin"
}{
	
	\relative c' {
\override Score.BarNumber.break-visibility = ##(#f #f #f)

\override Staff.TimeSignature.stencil = ##f
	\time 2/2
	c'1 ~c1 ~c1~c1
	\time 1/4
	r4
	\time 2/2
	f,1 ~ f1 ~ f1 ~ f1 ~ f1 ~ f1
	\time 5/4
	r4 c'1
	}	
}

\new Staff \with {
  instrumentName = #""
  shortInstrumentName = #""
  midiInstrument = "Violin"
}{
	
	\relative {
\override Staff.TimeSignature.stencil = ##f
	\clef bass
	\time 2/2
	c1 d e f
	\time 1/4
	r4
	\time 2/2
	g1 a b a g f 
	\time 5/4
	r4 c1
	\bar "|."
	}	
}
>>

>>
}