from progressbar import ProgressBar
import time
pbar = ProgressBar(maxval=100)
pbar.start()
for i in range(1, 100):
    pbar.update(i)
    time.sleep(0.3)
pbar.finish()