try:
   hours = float(input('Enter Hours: '))
   rate = float(input('Enter Rate: '))

   if hours > 40:
       reg_pay = (40 * rate)
       ot_pay = ((hours-40) * (rate * 1.5))
       total_pay = reg_pay + ot_pay
       print('Regular pay (for 40 hrs.): ', reg_pay)
       print('Overtime pay (for the hours over 40 hrs.: ', ot_pay)
       print('Total pay: ', total_pay)
   else:
       total_pay = (hours * rate)
       print('Total pay: ', total_pay)
except:
   print('Enter \'Hours\' and \'Rate\' in numbers')
