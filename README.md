# Курс лекций по Теории вероятностей и математической статистике Университета "Geekbrains" и практические задания к ним.

## Семинар 1. Случайные события. Условная вероятность. Формула Байеса. Независимые испытания

### Практическое задание к Семинару 1.
1. Из колоды в 52 карты извлекаются случайным образом 4 карты.  
   a) Найти вероятность того, что все карты – крести.   
   б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.  
2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?  
4. В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?  
5. В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?  

## Лекция 2. Дискретные случайные величины. Закон распределения вероятностей. Биномиальный закон распределения. Распределение Пуассона.  

### Практическое задание к Семинару 2.  
1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.  
2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. В жилом комплексе после ремонта в один день включили 5000 новых лампочек. Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?  
3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?  
4. В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые? Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?  

## Семинар 3. Описательная статистика. Качественные и количественные характеристики популяции. Графическое представление данных.  

### Практическое задание к Лекции 3.  
1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать (желательно без использования статистических методов наподобие std, var, mean)  
   а) среднее арифметическое,  
   б) среднее квадратичное отклонение,  
   в) смещенную и несмещенную оценки дисперсий для данной выборки.  
2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?  
3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. Найти вероятность того, что выстрел произведен:  
   a) первым спортсменом,   
   б) вторым спортсменом,  
   в) третьим спортсменом.
4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию. Какова вероятность, что он учится:  
   a) на факультете A,  
   б) на факультете B,  
   в) на факультете C?  
5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:  
   а) все детали,  
   б) только две детали,  
   в) хотя бы одна деталь,  
   г) от одной до двух деталей?  

## Урок 4. Непрерывные случайные величины. Функция распределения и плотность распределения вероятностей. Равномерное и нормальное распределение. Центральная предельная теорема.  

### Практическое задание к Лекции 4.
1. Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800]. Найдите ее среднее значение и дисперсию.  
2. О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2. Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5? Если да, найдите ее.  
3. Непрерывная случайная величина X распределена нормально и задана плотностью распределения f(x) = (1 / (4 * sqrt(2*pi))) * (exp(-((x+2)^2) / 32)). Найдите:  
   а) M(X)  
   б) D(X)  
   в) std(X) (среднее квадратичное отклонение)  
4. Рост взрослого населения города X имеет нормальное распределение. Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см. Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:  
   а) больше 182 см.;  
   б) больше 190 см.;  
   в) от 166 см. до 190 см.;  
   г) от 166 см. до 182 см.;  
   д) от 158 см. до 190 см.;  
   е) не выше 150 см. или не ниже 190 см.;  
   ё) не выше 150 см. или не ниже 198 см.;  
   ж) ниже 166 см.?  
5. На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

## Урок 5. Проверка статистических гипотез. P-значения. Доверительные интервалы. A/B-тестирование.  

### Практическое задание к Лекции 5.  
1. Известно, что генеральная совокупность распределена нормально, со средним квадратическим отклонением, равным 16. Найти доверительный интервал для оценки математического ожидания с надежностью 0.95, если выборочная средняя M = 80, а объем выборки n = 256.  
2. В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью, получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1 Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей, оценить истинное значение величины X при помощи доверительного интервала, покрывающего это значение с доверительной вероятностью 0,95.  
3. Утверждается, что шарики для подшипников, изготовленные автоматическим станком, имеют средний диаметр 17 мм. Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм, а дисперсия известна и равна 4 кв.мм.  
4. Продавец утверждает, что средний вес пачки печенья составляет 200 г. Из партии извлечена выборка из 10 пачек.  
Вес каждой пачки составляет: 202, 203, 199, 197, 195, 201, 200, 204, 194, 190. Известно, что их веса распределены нормально.  
Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?  

* <i>3,4 задачи решать через тестирование гипотезы</i>  

## Урок 6. Взаимосвязь величин. Параметрические и непараметрические показатели корреляции. Корреляционный анализ.  

### Практическое задание к Лекции 6.  
1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):  
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],  
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].  
Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy. Полученные значения должны быть равны. Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.  

2. Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:  
131, 125, 115, 122, 131, 115, 107, 99, 125, 111.  
Известно, что в генеральной совокупности IQ распределен нормально. Найдите доверительный интервал для математического ожидания с надежностью 0.95.  

3. Известно, что рост футболистов в сборной распределен нормально, с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2. Найдите доверительный интервал для математического ожидания с альфа =0,95   

## Урок 7.  Многомерный статистический анализ. Линейная регрессия.  

### Практическое задание к Лекции 7.  
1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):  
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],  
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].  
Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.  
2. Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).  
3. <i>Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).*</i>  

* Третье задание по желанию.  

## Урок 8. Дисперсионный анализ. Логистическая регрессия.  

### Практическое задание к Лекции 8.
1. Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов. Даны значения роста в трех группах случайно выбранных спортсменов:  
* Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.  
* Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.  
* Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
