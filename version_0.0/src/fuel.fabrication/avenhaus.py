# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:09:26 2017

@author: Jieun
"""

from scipy.stats import invgauss
from scipy.stats import norm

# rv = invgauss.ppf(0.95,mu) 
# a = 8/(2*rv)
# print a
# norm.ppf uses mean = 0 and stddev = 1, which is the "standard" normal distribution
# can use a different mean and standard deivation by specifiying the loc and scale arguments 
# norm.ppf(0.95, loc = 10, scale = 2)
#n = norm.ppf(0.95)
#n1 = norm.ppf(0.95)
#print n + n1
#check = norm.cdf(norm.ppf(0.95))
#print check
#print ''

# rv = invgauss.cdf(0.95, 8)
# rv1 = invgauss.cdf(0.95, 8)
# print rv
# print rv1
# print rv + rv1
# print 8/2.4
# print ''

# For inverse cdf 
# 1 - alpha = 0.981
# detection probability is not given...

## measured values 
# For Design A


inverse_1_alpha = norm.ppf(1-0.050)
inverse_1_beta = norm.ppf(0.90)
sum = inverse_1_alpha + inverse_1_beta
sigma = 8/sum
print sigma
print ''
print ''
# sq = 8
# sigma = sq/sum
# print sigma
# print ''

#print check
#cal= 1- check

# For Design B
#inverse_1_alpha_Design_B = norm.ppf(0.981)
#inverse_1_beta_Design_B = - inverse_1_alpha_Design_B + 0.940/1.189
#check2 = norm.cdf(inverse_1_beta_Design_B)
#print check2
#cal1 = 1- check2 
# print cal
#print cal1
## inspection values 
# inverse_1_alpha_expected = norm.ppf(0.981)
# inverse_1_beta_expected = inverse_1_alpha_expected - 0.90358/0.76235
# check3 = norm.cdf(inverse_1_beta_expected)
# `print check3



