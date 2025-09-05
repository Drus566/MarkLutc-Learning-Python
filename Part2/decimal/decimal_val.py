from decimal import Decimal

print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30'))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))

import decimal

print(decimal.Decimal(1) / decimal.Decimal(7)) # 28 цифр по умолчанию
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)) # Ближе к 0
