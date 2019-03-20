# Yid++ - the oylem's first programming shprach
BS"D

Yid++ is the oylem's first programming shprach written in yeshivish, for yidden, following Torah-true hashkafos.

For many years already, the oylem has had to use goyishe programming languages, which, as we all are aware, is a grave michshol. We all know the midrash, _lo shinu et shmam, leshonam, umalvusham_ -- as we all too well know, using the goyishe shprach can lead, lo aleinu, to all kinds of krum hashkafos and kilkulim.

Therefore, at the encouragement of _Gedolei Yisroel Shlit"a_, we took it upon ourselves to try to be metakein the pirtzos. _Baruch HaShem_, after extensive work and many personal meetings with the Gedoilim, who were constantly being mechazeik us towards this, and giving us Daas Torah, we were finally zoicheh to be mashlim the beta version of the Yid++ compiler.

The name Yid++ of course signifies the chashivus of always doing avoidas HaShem, and always doing hishtadlus, cheshbon hanefesh, and tikkun hamidos, to always go _michayil lechayil_, with hasmadah. It also signifies the support of C++, which certainly isn't because we followed the established formula laid out by yeshivishe music of just ripping off the goyishe version and then changing the words to make them more yeshivish. Certainly not that. 

Among the many new features of this language with the Daas Torah of _Gedolei Yisroel Shlit"a_:

* Static typing -- we were mekabel Daas Torah that dynamic typing is too postmodern and simply incompatible with a Torah-true hashkafa.
* Removing _Nivul Peh_.
* Removal of various keywords and methods that expressed krum hashkafos -- for example -- `while(1)` was strongly denounced by _Gedolei Yisroel Shlit"a_, and therefore we have replaced `while` with `until_mashiach_comes_or`.
* Special constants for counting people.
* Full backwards compatibility with C++11 standard library.

Right now, the compiler only runs on Unix based systems, the most emesdig architectures. Also, why spend extra money on Windows when you could use it to be mefarnes talmidei chachomim or to replace the dinged-up bumper on your 1993 Dodge Ram?

## Usage:
To install (Linux only for now), simply run:

```bash
wget -O - https://raw.githubusercontent.com/schorrm/ypp/master/install.sh | sudo bash
```

To run the compiler:

```bash
y++ [NAME OF FILE]
```

Language spec [available here](https://docs.google.com/spreadsheets/d/1K-3wx51FJzAsGC8_G9jYqV0_qpmuHGZrmJPrqlCiIPU/edit?usp=sharing)

BeChezkas Moshe Schorr

## Some code samples:

### Hello World

```
be_soymech_on <iostream>
holding shitta std;
bli_ayin_hara main () bh
	be_machriz << "hello world" << rabboisai;
  pasken 0;
shkoyach
```

### Sieve of Erastothenes

```
be_soymech_on <iostream>
be_soymech_on <vector>
be_soymech_on <cmath>

holding shitta std;

hearah this program takes a number and prints all primes up to that number, using the Sieve of Eratosthenes

bli_ayin_hara main () bh
	bli_ayin_hara limit;
	be_machriz << "enter the limit" << rabboisai;
	the_hock >> limit;
	limit++;
	
	vector<tzvei_dinim> primes (limit, emes);
	do_hishtadlus (bli_ayin_hara i = 2; i <= sqrt(limit); i++) bh
		do_hishtadlus (bli_ayin_hara j=i*i; j < limit; j += i) bh
			primes[j] = nisht emes;
		shkoyach
	shkoyach
	
	do_hishtadlus (bli_ayin_hara i = 2; i < limit; i++) bh
		efsher (primes[i]) bh
			be_machriz << i << " ";
		shkoyach
	shkoyach
	be_machriz << rabboisai;
	pasken 0;
shkoyach
```

### Recursive Fibonacci: 

```
be_soymech_on <iostream>
be_soymech_on <cstdlib>
holding shitta std;

hearah recursive fibonacci
bli_ayin_hara fibonacci (bli_ayin_hara x) bh
	efsher (x == 1 || x == 0) pasken x;
	pum_fakert pasken fibonacci(x-1) + fibonacci(x-2);
shkoyach

bli_ayin_hara main (bli_ayin_hara argc, oys *argv[]) bh
	bli_ayin_hara index = atoi(argv[1]);
	be_machriz << fibonacci(index) << rabboisai;
	pasken 0;
shkoyach
```
