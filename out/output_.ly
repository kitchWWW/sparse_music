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

s4. b8 \(c'4\) s4 
 s4. g'8 \(a'4\) s4 
 s2 g'4 s4 
 s2 s4 a'4 \( 
   ~ a'4   bes'4\) s4 s2 
   \break  s4. f'4 \(e'4\) s8 
 s2 b'4 \( a'4 
 d''4\) s4 s2 
 s4. a'8 \(b'4\) s4 
 s4. a'8 \(aes'4\) s4 
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