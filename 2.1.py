mätanställning=int(input('mätanställng i dag?:'))
gammal_mätanställning=int(input('mätanställning för ett år sedan?:'))
bensin_förbrukats=float(input('liter bensin som förbrukats under år?'))
antal_körda_mil=mätanställning-gammal_mätanställning
liter_per_mil=bensin_förbrukats/antal_körda_mil
print('antal körda mil:' , antal_körda_mil)
print('antal liter bensin:', bensin_förbrukats)
print('förbrukning per mil:', liter_per_mil)