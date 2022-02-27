def pyalu(model_no):
  d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13 = model_no

  z=     (d0+12)
  z=z*26+(d1+10)
  z=z*26+(d2+8)

  a=0 if (d3+4)==d4 else 1
  z=z*(25*a+1)+(d4+3)*a

  z=(z*26)+(d5+10)

  b=0 if (d6-6)==d7 else 1
  z=z*(25*b+1)+(d7+13)*b

  c=0 if (z%26-15)==d8 else 1
  z=(z//26)*(25*c+1)+(d8+8)*c

  d=0 if (z%26-15)==d9 else 1
  z=(z//26)*(25*d+1)+(d9+1)*d

  e=0 if (z%26-4)==d10 else 1
  z=(z//26)*(25*e+1)+(d10+7)*e

  f=0 if (d11+1)==d12 else 1
  z=z*(25*f+1)+(d12+9)*f

  g=0 if (z%26-12)==d13 else 1
  z=(z//26)*(25*g+1)+(d13+9)*g
  # Invariant: z==0
  return z
