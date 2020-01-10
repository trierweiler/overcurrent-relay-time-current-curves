import matplotlib.pyplot as plt
from gtr.my_funcs import iec_relay

# TB-01: Relay BBC IC 91 
RTC = 400 / 5
tb01_relay = iec_relay(PU=3.00*RTC, DT=0.2, curve_type='EI', DI=1440)
current_tb01, time_tb01 = tb01_relay.time_current_curve()

# LT 66 kV MD-IPU: Relay BBC IC 91 
RTC = 400 / 5
lt66_relay = iec_relay(PU=3.00*RTC, DT=0.4, curve_type='EI')
current_lt66, time_lt66 = lt66_relay.time_current_curve()

# TD-01, TD-02: Relay Inepar ID
RTC = 800 / 5
td_relay = iec_relay(PU=1.25*RTC, DT=0.45, curve_type='NI')
current_td, time_td = td_relay.time_current_curve()

# Plotting
plt.plot(current_tb01, time_tb01, 'bo-', markersize=3)
plt.plot(current_lt66, time_lt66, 'ro-', markersize=3)
plt.plot(current_td, time_td, 'go-', markersize=3)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Current (A)', fontsize='x-large')
plt.ylabel('Time (s)', fontsize='x-large')
plt.title('Ground overcurrent curves', fontsize='xx-large')
plt.ylim(10**-2, 10**3)
plt.xlim(10**2, 10**4)
plt.grid(which='both')

plt.legend(['TB-01', 'LT 66 MD-IPU', 'TD-01/02'], fontsize='xx-large')
