import rf
import numpy as np
cal = rf.CalEar(433.9e6)
#cal.plot_psd()

#cal.plot_multi_rss_live(433.91e6, 434.16e6, 2e4)
freqtx = [434.16e6] ## [433.9e6] # [434.16e6] #  [434.16e6] #
#cal.get_max_rss_in_freqspan(freqtx, 2e4)
# cal.make_test(5.0)
# cal.plot_multi_rss_live(433.91e6, 434.16e6)


# rss, var = cal.measure_rss_var(freqtx, 2e4, 10.0)
# alpha, xi = cal.get_model(rss, var)

#print ('Tx freq : ' + str(freqtx/1e6) + 'MHz, alpha = ' + str(alpha) + ' xi = ' + str(xi))


# messung kw 43    alpha = 0.123262770536  , xi = 28.4340027272 @ 433,91MHz
# messung 25.10.16 alpha = 0.0939750617382 , xi = 28.2926626424 @ 433,91MHz
# messung 25.10.16 alpha = 0.103343746736  , xi = 27.3188771771 @ 433,91MHz
#
# messung 25.10.16 alpha = 0.0874479464684 , xi = 23.8654845692 @ 434,16MHz
# messung 25.10.16 alpha = 0.0880381844913 , xi = 23.8442108093 @ 434,16MHz

# messung laengs
# messung 26.10.16 alpha = 0.12615852725  , xi = 28.2177151396 @ 433,91MHz
# messung 26.10.16 alpha = 0.117592701848 , xi = 11.9628114874 @ 434,16MHz



alpha = [0.12615852725, 0.117592701848]
xi = [28.2177151396, 11.9628114874]
freqtx = [433.91e6, 434.16e6]
freqspan = 2e4
freqcenter = 434.0e6
txpos = np.array([[0.0, 0.0],
                  [80.0, 0.0]])  #

# mat_test = np.array([[1,2], [3, 4]])
# print('mat_out' + str(mat_test))

# print('txpos' + str(txpos))
# freqmax, rssmax = cal.get_max_rss_in_freqspan(freqtx, 2e4)
# print ('freq_max ' + str(freqmax) + ' rss_max ' + str(rssmax))

loc = rf.LocEar(alpha, xi, freqtx, freqspan, freqcenter)
# loc.calibrate()
loc.map_path_ekf(txpos)
