
## 1. IP to CIDR
This is probably this worst question to deal with because it takes a bit of understanding of the logic.

```python

def ipToCIDR(self, ip: str, n: int) -> List[str]:
	def ip_to_int(ip):
		p1, p2, p3, p4 = ip.split('.')

		p1_int = int(p1) << 24
		p2_int = int(p2) << 16
		p3_int = int(p3) << 8
		p4_int = int(p4) << 0
		return p1_int + p2_int + p3_int + p4_int

	def int_to_ip(int_val):
		p4 = 255 & (int_val >> 0)
		p3 = 255 & (int_val >> 8)
		p2 = 255 & (int_val >> 16)
		p1 = 255 & (int_val >> 24)
		return f'{p1}.{p2}.{p3}.{p4}'
	
	res = []
	start = ip_to_int(ip)
		# clear all, except right most bit
		# n     = 00001100  (decimal 12)
		# -n    = 11110100  (decimal -12)
		# n & -n = 00000100 (decimal 4)

	while n:
		# Largest block size that aligns with current start IP
		alignment = int(start & -start)
		if alignment == 0:
			ips_block_size = 32  # no alignment constraint
		else:
			ips_block_size = int(log2(alignment))
		
		# Largest block that fits in remaining n IPs
		ips_to_fit_based_on_n = int(log2(n))

		# Take the smaller one to stay safe
		host_bits = min(ips_block_size, ips_to_fit_based_on_n)
		prefix_size = 32 - host_bits

		res.append(f'{int_to_ip(start)}/{prefix_size}')
		ips_created = pow(2, host_bits)

		n -= ips_created
		start += ips_created
	return res
```

