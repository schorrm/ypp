# ypp - The Yid++ Compiler 
BS"D

Yid++ is the oylem's first programming shprach written in yeshivish, for yidden, following torah-true hashkafos.

To install (Linux only for now), simply run:

```bash
wget -O - https://raw.githubusercontent.com/schorrm/ypp/master/install.sh | sudo bash
```

To run the compiler:

```bash
y++ [NAME OF FILE]
```

Language spec available here: https://docs.google.com/spreadsheets/d/1K-3wx51FJzAsGC8_G9jYqV0_qpmuHGZrmJPrqlCiIPU/edit?usp=sharing

BeChezkas Moshe Schorr

# Some code samples:

Hello World

```
be_soymech_on <iostream>
holding shitta std;
bli_ayin_hara main () bh
	be_machriz << "hello world" << rabboisai;
  pasken 0;
shkoyach
```

Sieve of Erastothenes

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

Recursive Fibonacci: 

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
