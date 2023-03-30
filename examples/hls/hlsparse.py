import sys
import threefive


def do(mesg):
    print(f"cue: {mesg}")
    tf = threefive.Cue(mesg)
    tf.decode()
    tf.show()


with open(sys.argv[1], "r", encoding="utf-8") as manifest:
    hls_time = duration = cue_out = cue_in = 0
    while manifest:
        l = manifest.readline()
        if not l:
            break
        if l.startswith("#EXT-X-CUE-OUT:"):
            cue_out = hls_time
            duration = float(l.split(":")[1])
            cue_in = hls_time + duration
            print(f"hls time: {hls_time}")
            print(f"cue out: {cue_out}")
            print(f"duration: {duration}")
            print(f"cue in: {cue_in}")
        ##EXTINF:4.000000,
        if l.startswith("#EXTINF:"):
            t = l.split(":")[1].split(",")[0]
            t = float(t)
            hls_time += t
            next_line = manifest.readline()[:-1]
            if not (next_line.startswith("#")):
                print(f"Segment: {next_line} @ {hls_time}")
            # EXT-X-SCTE35:CUE=
        if l.startswith("#EXT-X-SCTE35"):
            mesg = l.split("CUE=")[1]
            do(mesg)
        if l.startswith("#EXT-OATCLS-SCTE35:"):
            mesg = l.split("#EXT-OATCLS-SCTE35:")[1]
            do(mesg)
        ##EXT-X-DATERANGE:ID="splice-6FFFFFF0",START-DATE="2014-03-05T11:15:00Z",PLANNED-DURATION=59.993,SCTE35-OUT=0xFC002F0000000000FF000014056FFFFFF000E011622DCAFF000052636200000000000A000829896F50000008700000000
        if l.startswith("#EXT-X-DATERANGE:"):
            for chunk in l.split(","):
                k, v = chunk.split("=")
                if k.startswith("SCTE35"):
                    cue = threefive.Cue(v)
                    cue.decode()
                    cue.show()
