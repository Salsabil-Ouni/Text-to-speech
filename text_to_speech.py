from gtts import gTTS

text="Generative AI Designs DNA Sequences to Switch Genes On and Off. Nestled in our genomes are tiny sequences with immense power to control nearby genes. Known as cis-regulatory elements, or CREs, these DNA sequences can switch neighboring genes on or off"
language='en'
obj=gTTS(text=text,lang=language,slow=False)
obj.save("speeched.mp3")