# Как компилировать программы для РК локально и запускать на эмуляторе

Пример простого цикла разработки.

Допустим, есть ваша программа [`rk86_example.asm`](https://github.com/begoon/rk86-example/blob/main/rk86_example.asm):

    org 0
    
    lxi h, msg
    call 0f818h
    jmp 0f86ch
    
    msg db 'EXAMPLE', 0dh, 0ah, 0

Создаете репозиторий [`rk86-example`](https://github.com/begoon/rk86-example) на GitHub.

Кладете туда исходник и создаете [`Makefile`](https://github.com/begoon/rk86-example/blob/main/Makefile):

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

Далее цикл разработки выглядит так:

  - файл `rk86_example.asm` редактируется локально
  - `make` или `make build` компилиет файл `rk86_example.rom` и создаст 
    выходной текстовый файл `rk86_example.bin`
  - `rk86_example.bin` тебе надо закоммитить и сделать `push`, чтобы файл
    ушел на github и стал [доступен для скачивания](https://raw.githubusercontent.com/begoon/rk86-example/main/rk86_example.bin) в формате raw
  - `make run` запускает файл в эмуляторе

Для данного `Makefile` требуется ассемблер [zasm](https://k1.spdns.de/Develop/Projects/zasm/Documentation/) и программа [rk86_hex.py](https://github.com/begoon/rk86-example/blob/main/rk86_hex.py).

# Как собрать [zasm](https://k1.spdns.de/Develop/Projects/zasm/Documentation/)

Проверялось на Mac.

    cd your/development/folder
    git clone git@github.com:Megatokio/zasm.git
    git clone git@github.com:Megatokio/Libraries.git
    cd zasm
    make
    ./zasm

Должно вывести что-то вроде:

    zasm - 8080/z80/z180 assembler (c) 1994 - 2021 Günter Woigk.
    version 4.4.8, 2021-03-09, for Unix-MacOSX.

