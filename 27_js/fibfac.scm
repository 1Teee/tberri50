(define fac (lambda (n) 
if (= n 0) n (* n fac(- n 1))))

fac(0)
fac(1)
fac(2)
fac(3)
fac(4)
fac(5)
fac(6)


(define fib (lambda (n)
if (= n 0) n (+ n fib(- n 1))))


fib(0)
fib(1)
fib(2)
fib(3)
fib(4)