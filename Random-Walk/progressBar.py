import time

def printProgressBar(iteration, total, starting_time, prefix='', suffix='', decimals=2, length=30, fill='#', printEnd="\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    eta = int((time.time()-starting_time)*(total/(iteration+1)-1))
    eta = time.strftime('%H:%M:%S', time.gmtime(eta))
    print(f'\r{prefix} |{bar}| {percent}% {suffix}',
          f"ETA: {eta}", end=printEnd)
    if iteration == total:
        print(f'{prefix} |{bar}| {percent}% {suffix} ',f"({round((time.time()-starting_time),5)} seconds)")
