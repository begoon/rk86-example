TARGET=rk86_example
RUN=https://rk86.ru/index.html?file=

all: build hex

build:
	zasm --asm8080 -l0 $(TARGET).asm

hex:
	python rk86_hex.py -i $(TARGET).rom -o $(TARGET).bin

run:
	open $(RUN)https://raw.githubusercontent.com/begoon/rk86-example/main/$(TARGET).bin

clean:
	-rm $(TARGET).rom
