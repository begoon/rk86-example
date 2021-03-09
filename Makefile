TARGET=rk86_example

all: build hex

build:
	zasm --asm8080 -l0 $(TARGET).asm

hex:
	python rk86_hex.py -i $(TARGET).rom -o $(TARGET).bin

run:
	open https://rk86.ru/index.html?file=https://gist.githubusercontent.com/begoon/7c98577dfc27c41483ef5f5e7857587d/raw/rk86_example.bin

clean:
	-rm $(TARGET).rom
