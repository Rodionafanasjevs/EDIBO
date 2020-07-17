# Команда pwd - это очень простая утилита, которая позволяет вывести в терминал путь к текущей папке.

-L, --logical - брать директорию из переменной окружения, даже если она содержит символические ссылки;

-P - отбрасывать все символические ссылки;

--help - отобразить справку по утилите;

--version - отобразить версию утилиты.

Команда ls - посмотреть разрешения для файлов и папок; быстро посмотреть что находится в папке. Чтобы посмотреть список файлов в папке linux для точно заданной папки, вам нужно указать путь к ней. Например, смотрим содержимое корневой папки ls / или папки /bin

В виде списка с максимальным количеством информации ls -l

-a - отображать все файлы, включая скрытые, это те, перед именем которых стоит точка;

-A - не отображать ссылку на текущую папку и корневую папку . и ..;

--author - выводить создателя файла в режиме подробного списка;

-b - выводить Escape последовательности вместо непечатаемых символов;

--block-size - выводить размер каталога или файла в определенной единице измерения, например, мегабайтах, гигабайтах или 
килобайтах;

-B - не выводить резервные копии, их имена начинаются с ~;

-c - сортировать файлы по времени модификации или создания, сначала будут выведены новые файлы;

-C - выводить колонками;

--color - включить цветной режим вывода, автоматически активирована во многих дистрибутивах;

-d - выводить только директории, без их содержимого, полезно при рекурсивном выводе;

-D - использовать режим вывода, совместимый с Emacs;

-f - не сортировать;

-F - показывать тип объекта, к каждому объекту будет добавлен один из специализированных символов */=>@|;

--full-time - показывать подробную информацию, плюс вся информация о времени в формате ISO;

-g - показывать подробную информацию, но кроме владельца файла;

--group-directories-first - сначала отображать директории, а уже потом файлы;

-G - не выводить имена групп;

-h - выводить размеры папок в удобном для чтения формате;

-H - открывать символические ссылки при рекурсивном использовании;

--hide - не отображать файлы, которые начинаются с указанного символа;

-i - отображать номер индекса inode, в которой хранится этот файл;

-l - выводить подробный список, в котором будет отображаться владелец, группа, дата создания, размер и другие параметры;

-L - для символических ссылок отображать информацию о файле, на который они ссылаются;

-m - разделять элементы списка запятой;

-n - выводить UID и GID вместо имени и группы пользователя;

-N - выводить имена как есть, не обрабатывать контролирующие последовательности;

-Q - брать имена папок и файлов в кавычки;

-r - обратный порядок сортировки;

-R - рекурсивно отображать содержимое поддиректорий;

-s - выводить размер файла в блоках;

-S - сортировать по размеру, сначала большие;

-t - сортировать по времени последней модификации;

-u - сортировать по времени последнего доступа;

-U - не сортировать;

-X - сортировать по алфавиту;

-Z - отображать информацию о расширениях SELinux;

-1 - отображать один файл на одну строку.

CD- Позволяет перейти из текущего каталога в указанный. Если запустить без параметров - возвращает в домашний каталог. Вызов 
с двумя точками возвращает на уровень вверх относительно текущего каталога. Вызов с тире (cd -) возвращает к предыдущему каталогу.

MKDIR - Создание новых каталогов. Наиболее удобная опция -p (Parents), позволяет создать всю структуру подкаталогов одной командой, даже если они ещё не существуют.

Cd Deskrop ; mkdir ABS – создание папки

Ls Desktop/| wc –m – символы

-c биты

-l строки

LN - Создает жёсткие или символические ссылки на файлы.

DU - Показывает размер файла или каталога. -h (Human), которая преобразует размеры файлов в легко читаемый формат, -s (Summarize), которая выводит минимум данных, и -d (Depth), устанавливающая глубину рекурсии по каталогам.

DF - Анализатор дискового пространства. По умолчанию вывод достаточно подробный: перечислены все файловые системы, их размер, количество использованного и свободного пространства. -h 

DD - команда терминала для копирования и преобразования файлов.

DATE - В отличие от time, делает именно то, чего вы от неё и ожидаете: выводит дату и время в стандартный вывод.

PS / PGREP - чтобы уничтожить процесс, нужен его идентификатор. Один из способов получить его, это утилита ps, которая печатает информацию о запущенных процессах.

Ps aux | pgrep chrome - фильтр

↑↑↑↑ - Windows XP

Cd ; pwd; Tab+Tab – нахождение всех папок

Ls | head –n 3 – первые три строчки

Wc – для подсчета слов, строк, байтов линии, слова, байты

Cd ~ - вернуться в начала

Java –version – все о программе

  * Python:

Echo $b - вывести

Echo $a$z – умножить

Echo $((a+b)) - объед.2 строки

Sum = $(($a+$b)) ; echo sum – через переменные

Echo $a$z EUR – в евро

Echo $a$z EUR > a.txt – в текст

  * Ls – l a.txt

Cat a.txt

Head a.txt

Tail a.txt

  * Cntl+l или  clear - удалить все
  * C:/  ;  с^  ;  Cntl+d – выйти из терминала
  * Init 0 – выключить пк

Все мы используем команду cd .. для перехода в родительскую директорию. А для перехода к предыдущей директории можно использовать команду cd -

  * test@linoxide:~/Downloads$ cd -
 /home/eyramm
test@linoxide:~$ cd -
 /home/eyramm/Downloads
test@linoxide:~/Downloads$

  * Чтобы повторить предыдущую команду, просто введите !!

$ apt install vlcnvm i 12

  * $ sudo !!
 
 sudo apt install vlc

Для того, чтобы выполнять команду до тех пор, пока она не будет успешно завершена, используйте код возврата команды в такой конструкции:

  * while ! [command]; do sleep 1; done

$ while ! ./run.sh; do sleep 1; done

cat: run.sh: No such file or directory

cat: run.sh: No such file or directory

linoxide.com

Команда в этом примере будет повторяться до тех пор, пока не будет найден файл run.sh и его содержимое не будет выведено на экран.

  * Чтобы наблюдать за ходом передачи файла, воспользуйтесь командой pv

$ pv access.log | gzip > access.log.gz
 
 611MB 0:00:11 [58.3MB/s] [=> ] 15% ETA 0:00:59

Планировать задания в Linux можно с помощью команды at

echo wget https://sample.site/test.mp4 | at 2:00 PM

Вызвав команду ls, или что-нибудь ещё, выводящее данные на экран, можно столкнуться с длинными списками, для просмотра которых требуется продолжительный скроллинг. То, что выводится на экран, легко можно организовать в виде таблицы с помощью команды column -t

$ cat /etc/passwd | column –t

    • Команда clear очищает экран терминала. Комбинация клавиш Ctrl + L позволяет добиться того же самого быстрее.
    • Комбинация клавиш Alt + . позволяет перемещаться по ранее введённым командам. Комбинация клавиш Ctrl + U убирает из строки всё то, что уже в неё введено. Например, можете это попробовать для очистки введённого в командной строке пароля.
    • Для инкрементального обратного поиска по истории команд используйте комбинацию клавиш Ctrl + R.

---

# Day 2

cp 1.txt ./ABC/2.txt — копировать один файл ткст в другой файл 

> ls 

cp 1.txt ABC/2.txt

cp 1.txt /ABC/2.txt

cp 1.txt 2.txt\

> cp 1.txt 2.txt

cp 1.txt 2.txt

ls

nano 2.txt — запустить редактор где ьудут изменения

cat 2.txt — вывести содержимое файла

rm 2.txt - удалить

m 1.txt

  * тоже самое

nano 1.txt

ls

cp 1.txt ./ABC/2.txt

cp 1.txt ABC/2.txtls

cp 1.txt ABC/2.txt
 
 cp 1.txt /ABC/2.txt

cp 1.txt 2.txtcp 1.txt 2.txt

cp 1.txt 2.txt

ls

nano 2.txt

cat 2.txt

rm 2.txt

rm 1.txt

ls

  * nano 1.txt

cat 1.txt

ls -l

hexdump c 1.txt – вывести слдеажтиое в 6 ричном виде

~$ xxd -b 1.txt - создаёт представление файла в виде шестнадцатеричных кодов или выполняет обратное преобразование.  -b 
значит в bайтах

1 byte = 8 bits

(0/1) - 2 states => inuque codes 2^8=256

[tab](https://lh3.googleusercontent.com/proxy/42VsTkLRxfFPsUcO07Vm6GE6al8E2TyzHFqRplS5g-gGg_t5HnZKGm04SvKJLiwBZTElVqglk_MQ5XMZeH4CDoxVIh0XZNG0NwixDObwX0Lg-Dk)

  * echo $PATH – вывести всеъ переменных

/usr/local/anaconda3/bin:/opt/intelFPGA_lite/17.1/quartus/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin


nano 01.sh – создать файл скрипт

   * #!/bin/bash – прописали все строчки

mkdir DEF – создать вавку 

cd DEF - перейти

touch test.txt – создать файл в ткт

cd .. - выйти на щаг назад

cp DEF/test.txt ./test1.txt – копировать изсходя где н6аход. (pwd) откуда куда

chmod 744 first_script.sh -= дать права файлу
 

  * cd
git clone https://github.com/Rodionafanasjevs/EDIBO

ls

cd EDIBO

  * ls -lt – кланировали своего файла

vim 01.sh — редактор по типу nano

chmod +x 01.sh and chmod 777 — разрешение на редактирование

  * ./01.sh — заставить считать все что сделали в vim#! /bin/bash

Наш vim

  * #EJjam majas

cd

echo "dd"

a=3 b=4

echo $a+$b=$((a+b))

echo  `date`

копирование

esc + e + p+p+p…

PS1 = $
$

for i in {0..5}; do echo "$i"; done

---

# Day 3

Чтобы выключить компьютер из терминала, введите poweroff, а для перезагрузки — reboot.

df -h | grep dev

df -h | grep sda2

df -h | egrep sda2

df | egrep sda2

  * Grep — мощный файловый поисковик, также может использоваться для поиска и фильтрации внутри одного или нескольких файлов. Может искать любой тип строки в любом файле или списке файлов или даже выводить любую команду.

  * Grep так же может запросто подсчитать количество совпадений:

ifconfig | grep –c inet6

  * Egrep — это еще одна производная, которая означает «Расширенное глобальное
регулярное выражение».

  * Egrep очень полезен для поиска исходных файлов и других частей кода, если возникнет такая необходимость. Она может быть вызвана из регулярного grep, указав параметр -E.

  * Fgrep ищет файл или список файлов для фиксированной строки шаблона. Это то же самое, что и grep -F. Обычный способ использовать fgrep — передать ему файл шаблонов:

fgrep –f file_full_of_patterns.txt file_to_search.txt

man grep – помогает найти комбинации

Sed - потоковый редактор и конечный редактор (неинтерактивный текстовый редактор) для автоматического изменения файлов. 

df --output=pcent /dev/sda2

stringl=$(df -h | egrep sda2)

sda="$(echo $string1|cut -d" " -f5)"

sda="$(echo $stringl |cut -d" " -f5)"

echo $sda

  * sda="$(echo $stringl |cut -d" " -f5)"

df -h

  * sda=$(df -h | egrep sda2)

num1="$(echo $sda |cut -d" " -f2)"

echo $num1

99G

  * sda=$(df | egrep sda2)

num1="$(echo $sda |cut -d" " -f2)"

num2="$(echo $sda |cut -d" " -f3)"

echo $num1 $num2

103292152 66612096

  * num2="$(echo $sda |cut -d" " -f3)"

num1="$(echo $sda |cut -d" " -f3)"

num2="$(echo $sda |cut -d" " -f4)"

echo $(($num1 / $num2))

2 

  * df -h |egrep sda2 | awk '{print ($3)/$2*100 "%"}'\

df -k /home | awk '{ print $5 }'|grep %|cut -d% -f 1

df /home/|tr -s ' ' |cut -d' ' -f5|tail -n1

df /home | awk '{ print $5 }' | sed 's/|//'

$ bc <<<" scale=4; (($a/$b)*100)"

68%

  * System observation interval - 1 sec.
    
    1. Input - df command
    2. Output - Data files: 02.dat and 03.dat
    3. Observation length
        1. - 1 min. (02.dat)
        2. - forever (03.dat)

echo `awk "BEGIN {printf\"%.2f\n\",66290508/103292152*100}"`"%"

  * #! /bin/bash

b=$(df --output=size /dev/sda2 | tail -n 1)

c=$(df --output=avail /dev/sda2 | tail -n 1) d=$(((b-c)*100/b))

while sleep 1; do echo `date`; echo $d | tee -a 02.dat ; done

# DAY 5 -  Gnuplot

ctrl d and exit

touch 1.sh

vim 1.sh

  * #! bin/bash/

echo > 2.txt

for i in {0..1000};

do echo $((i)) $((i*i)) $((i*i*3)) >> 2.txt;

done

 * touch 2.txt

bash 1.sh

cat 2.txt

splot "2.txt"

Allwork(Gnuplot1)

  * plot "2.txt"

Allwork(Gnuplot2)

  * plot "2.txt" u 4:4, "2.txt" u 1:4 w l

Allwork(Gnuplot3)

  * plot "2.txt" u 4:4, "2.txt" u 2:4 w l

Allwork(Gnuplot4)

  * set polar

plot cos(2*t) with lines lt 7 dt 3 lw 3 ,sin(4*t) lt 12 lw 3\

Allwork(Gnuplot5)

---

# DAY 6 - 9

  * sk bin hex
  
0 0000 0

1 0001 1

2 0010 2

3 0011 3

4 0100 4

5 0101 5

6 0110 6

7 0111 7

8 1000 8

9 1001 9

10 1010 A

binary.sh

[stackoverflow](https://stackoverflow.com/questions/10822790/can-i-call-a-function-of-a-shell-script-from-another-shell-script)

function convert () # (Val Base)

{
 
 val=$1
 
 base=$2
 
 result=""
  
  while [ $val -ne 0 ] ; do
 
 result=$(( $val % $base ))$result #residual is next digit
  
  val=$(( $val / $base ))
 
 done
  
  echo -n $result

}

or

binary2.sh

[stackexchange](https://unix.stackexchange.com/questions/223338/convert-a-value-into-a-binary-number-in-a-shell-script)

toBinary(){
   
   local n bit
    
    for (( n=$1 ; n>0 ; n >>= 1 ));
    
    do  bit="$(( n&1 ))$bit"; done
    
    printf "%s\n" "$bit"

}

  * # terminal

source binary.sh

convert 64 2 (convert=function from binary.sh, 64=val, 2=base)

---

Task:

Create a BASH script ready to convert WHOLE DECIMAL NUMBER as input into BINARY NUMBER on the terminal output.

Restrictions: only native BASH variables-related, conditional, and loopwise operations allowed.

Only allowed math construction is like

---

file1:

#! /bin/bash

echo $1 $2

terminal:

./file1 some any -> to execute 

output:

some any

# VIM
       Commands:
                   Mods:
    • ESC -> Normal mode
    • i -> insert mode
    • v -> visual mode (select text)
                       Movement:
    • h,j,k,l - left down up right
    • 0 - to the start of the line
    • [1..N]w - move to the start of next N word
    • [1..N]e - move to the end of next N word
    • g - the start of file. G - the end of file
                       Editor tools:

    • n - next forward. N - next backward
    • u - undo previous command. U - return original line
    • CTRL + r(R) - rollback of rollback (decline u)
    • CTRL + W(x2)- for change work window
                       Edit text:
    • r[character] - change next character after caret with [ch]. R - for changing more than one character
    • x - remove next symbol. X - remove previus symbol
    • y - copy. yw - copy one word
    • p - paste
    • a - add text. A - add text from the end of the line
    • o - insert new line + Insert mode. O - insert new line before caret + Insert mode.
    • j - move caret on the next line. j$ - move caret to the end of next line
    • w - next word
    • e - next word's end
    
    d (delete) [operator] object
    • d - delete line. D - delete line starting of caret place
    • dw - delete word with space
    • d[1..N]w - delete N words
    • de - delete word without space
    • d^ - delete text from the start line to the caret
    • d& - delete text from caret to the end of the line
    • dd - delete line (save to the buffer)
    • [1..N]dd - delete N lines
    
    c (replace) [N] + c + object or c + [N] object
    • ce - cut the end of word and switch on the INSERT mode
    • c + [w/e/^/&]
  
                         * Comands in normal mode:
    • :q! - exit without saves
    • :wq! - save file and exit. (write quit)
    • :w filename - to save filename. v + j,k + w filename
    • :! outer command - execute outer command (:!ls / :!ls / :rm filename>
    • :r filename - reading file and insert it. :r !ls - reading output outer command.
                       Other:
    • CTRL + g - [path|status|i-string|% of file].
    • G - end of the file.
    • [N]G - go the N line

                       Searching:
    • /<characters/word> - searching forward. ( Use n or N )
    • ?<characters/word> - searching backward. ( Use n or N )

    • CTRL + o(O) - move back before searching
    • CTRL + i(I) - move forward before searching ?

    • % before (,{,[ - find pair

    • :s/was/became - for change 'was' to 'became' one time
    • :s/was/became/g - for change 'was' to 'became' inside string
    • :#,#s/было/стало/g - these #,# are numbers of strings.
    • :%s/было/стало/gc - for change 'was' to 'became' inside entire file.
               
                 * Set Proporties:
    : set command_name \c - command only for one searching
    
    • :set ic - ignore text case. :set noic - set case
    • :set hls is - hlsearch and incsearch - searching highlights. :nohlsearch - no hightlights
                   Help:
    • F1 or :help - help
    • Normal mode command :help x
    • Visual mode command v_ :help v_u
    • Insert mode command i_ :help i_
    • Command-line command : :help :quit
    • Command-line editing c_ :help c_
    • Vim command argument - :help -r
    • Option ' :help 'textwidth'
    • Regular expression / :help /[
           
           Anki:
    • https://ankiweb.net/shared/info/1557429385(https://ankiweb.net/shared/info/1557429385)
    • https://ankiweb.net/shared/info/553269875(https://ankiweb.net/shared/info/553269875)

---

# PYTHON

#! usr/bin/python3.6

print(5 + 10)

print(3 * 7, (17 - 2) * 8)

a = input()

b = input()

s = a + b

print(s)

  * Moduls

x = int(input())

if x > 0:
   
   print(x)

else:
   
   print(-x)

x = int(input())

y = int(input())

if x > 0:
   
   if y > 0:    TAB
      
      print("Первая четверть")
    else:      
        print("Четвертая четверть")
    else:
    if y > 0:         
        print("Вторая четверть")
    else:                  
        print("Третья четверть")

  * <


Меньше — условие верно, если первый операнд меньше второго.


Больше — условие верно, если первый операнд больше второго.

  * <=


Меньше или равно.

  * >=


Больше или равно.

  * ==


Равенство. Условие верно, если два операнда равны.

  * !=


Неравенство. Условие верно, если два операнда неравны.
 
 ---
 
a = int(input())

b = int(input())

if a % 10 == 0 or b % 10 == 0:
    
    print('YES')

else:
   
   print('NO')
   
   ---
 
# Функция

int(x) - Округляет число в сторону нуля. Это стандартная функция, для ее использования не нужно подключать модуль math.

round(x) - Округляет число до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до ближайшего четного числа.

round(x, n) - Округляет число x до n знаков после точки. Это стандартная функция, для ее использования не нужно подключать модуль math.

floor(x) - Округляет число вниз («пол»), при этом floor(1.5) == 1, floor(-1.5) == -2

ceil(x) - Округляет число вверх («потолок»), при этом ceil(1.5) == 2, ceil(-1.5) == -1

abs(x) - Модуль (абсолютная величина). Это — стандартная функция. Корни, логарифмы

sqrt(x) - Квадратный корень. Использование: sqrt(x)

log(x) - Натуральный логарифм. При вызове в виде log(x, b) возвращает логарифм по основанию b.

e - Основание натуральных логарифмов e = 2,71828...

  * #! /usr/bin/python3.8

def name():
	
 x = int(input('Input number below, please:\n'))
	
 print('Your number is:', x)

name()

---

# Github

mkdir DT4

cd DT4

ls

pwd

git init

git remote -v

git pull origin master

touch DT_Rodion.txt

vim DT_Rodion.txt

git add .

git commit -m "Rodion commit"

git config --global user.email "rodionafanasjevs@gmail.com"

git config --global user.name "Rodionafanasjevs"

git commit -m "Rodion commit"

git push origin master

# Python

printf 1 | hedump -x

printf 12 | hexdump -x

printf 120 | hd -x

printf AbC | hd -v

pwd

  * ./Python_work_DAY2.py

chmod +x Python_work_DAY2.py

./Python_work_DAY2.py

#! /usr/bin/python

for i in [1,100,'o']:
    
    print(i)
    
  * curl google.com

curl google.com | hexdum |less

dir(a) what you can do with this variable

a.reverse() (reverses the list)

a.sort() (sorts list by numerical values)

a.sort(reverse=True) (sorts the list in reverse(from highest to lowest))

a = {"ābols":"apple"} ({} dictionary)

a["ābols"] (shows apple)

a.update({"bumbieris":"pear"})

a.pop("ābols")

python -m http.server = launches python so you can view you directories (127.0.0.1:8000 or localhost:8000 - firefox) or (curl 127.0.0.1:8000 - bash)

vars() = shows all variables available

type(a) (shows what type is a (for example a = 1 is integer or a = 1.2 is float))

a.__ doc__

a.pop.__ doc__ (shows documentation about pop)

print(a.__ doc__)

a[0] (index shows first number)

idle & (opens python prompt or smthing)

---

# for i in range

for i in range(9): print(i)

1...10

for i in range(9): print(i,i)

1...8

1...8

  * for i in range(4,9): print(i,i*i)

4 16, 5 25, 6 36, 7 49, 8 64

for i in range(-4,9): print(i,i*i)

-4 16, -3 9, -2 4, -1 1, 0 0, 1 1, 2 4, 3 9

for i in range(-4,5): print('11') ; print('A')

11 A

11 A

for i in range(4):
  
  print("",i,"",end='')

0  1  2  3 

  * for i in range(5):
    
    print(i)
    
    print(i*i)
    print("hi")

0 0 hi, 1  1 hi, 2 4 hi,  3 9…

  * t = "Summa = %s"%(22)

t = "Summa = %s"%(33)

t = "Summa = %s"%(2,'EUR')

t = "Summa = %s"%(2,'EUR' )

t = "Summa = %s, valuta=%s"%(2,'EUR' )

t = "Summa = %s, valuta=%s, Janka = %s"%(2,'EUR',777 )

  * s = """

Godajamais x,

Jums ir pienacis naudas parvedums

ar vertibu y EUR

Lai sanemtu naudu, atsutit

iszinu ux telf. numuru z

Ciena,

atraitne

"""\

 * print("Hello")

f()

def f(x):

print("Hello"+11)

f(11)

def f(x):

print("Hello"+str11))

def f(x):

print("Hello"+str(11))

f(x)

def f(x):

print("Hello "+str(11)+" "+ x)

f('EDIBO')

f(22)

def f(x):

x = str(x)

print("Hello "+str(11)+" "+ x)

f(11)

f(22)

f('RTU')

f = open("a.dat" , "w") – creat new file

---

# Dotnet

HTML → C# → PHP → SQ
 
export NVM_DIR="$HOME/.nvm" && (
 
   * git clone https://github.com/nvm-sh/nvm.git "$NVM_DIR"
 
 cd "$NVM_DIR"
 
 git checkout `git describe --abbrev=0 --tags --match "v[0-9]*" $(git rev-list --tags --max-count=1)`

) && \. "$NVM_DIR/nvm.sh"

nvm i 12

  * Frontends - clock, nor.life

Backends - serviss

Qa – Manuali

Hybridapps

Unittest — наверное самый известный фреймворк для написания тестов в Python. Он очень прост в освоении и его легко начать использовать в вашем проекте.

Polyfills – в веб-программировании это код, реализующий какую-либо функциональность, которая не поддерживается в некоторых версиях веб-браузеров. Обычно представляет собой библиотеку JavaScript, которая реализует поддержку веб-стандарта HTML5 в версиях браузеров, где поддержка этих функций частично или полностью отсутствует. Это обеспечивает более или менее единообразное отображение веб-страниц в разных веб-браузерах

$(“H1”).text

Vanillajs

Regex

CI/CD

[validator](https://validator.w3.org/)


  # JS

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=, initial-scale=1.0">

<title>Document</title>

</head>

<body>

    * <h>Scooby dooby doo</h>

<script>

class TodayDateComponent extends HTMLElement {

constructor(){

super();

SetInterval(() => {

this.innerText = new Date();

}, 1000);

}

}

  * const comp = customElements.define('today-date', TodayDateComponent);

</script>

</body>

</html>


<!DOCTYPE html>

<html lang="en">

<head>
   
   <meta charset="UTF-8">
    
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
   <title>Document</title>

</head>

<body>
  
   * <h>Hello</h>
    
   <script>
       
 const a = document.querySelector('h1')
      
  a.addEventListener('click', () => alert('Hi,Rodion'))
    
  </script>

</body>

</html>
    
  * <!DOCTYPE html>

<html lang="en">

<head>
   
   <meta charset="UTF-8">
    
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
   <title>Document</title>

</head>

<body>
    
    <today-date>Yes</today-date>
    
    <script>
       // recepte Omlete izskatasPec Edina {
           //     constructor(confuguration){}
            //        this.color="green";
            //    }
         //   }
        //var o = new Omlete();
        //o.color = "green";
            //}
        class TodayDateComponent extends HTMLElement {
            constructor(){
                super();
                this.innerText=new Date();

            }
        }

        const comp = customElements.define('today-date', TodayDateComponent);
    </script>

</body>

</html>
