TARGET=rk86_example

all: build hex

build:
	zasm --asm8080 -l0 $(TARGET).asm

hex:
	python rk86_hex.py -i $(TARGET).rom -o $(TARGET).bin

clean:
	-rm $(TARGET).rom
