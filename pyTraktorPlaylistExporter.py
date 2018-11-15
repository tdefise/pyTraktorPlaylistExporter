import xml.etree.ElementTree as ET
import getopt
import sys

COLLECTION = r"C:\Users\Thomas.defise\Documents\Native Instruments\Traktor 2.11.3\collection.nml"
TRACK_LIST = []


def parse_collection(playlist):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(COLLECTION, parser=parser)

    for a in tree.iter(tag="NODE"):
        if a.get("NAME") == playlist:
            for z in a.iter(tag="PRIMARYKEY"):
                windows_path_track = z.get("KEY").replace("/:", "\\")
                TRACK_LIST.append(windows_path_track)

    return TRACK_LIST


def arg_processing(argv):
    playlist = ""
    try:
        opts, args = getopt.getopt(argv, "hp:", ["playlist="])
    except getopt.GetoptError:
        print("pyTraktorPlaylistExporter__.py -p <TraktorPlaylist>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-p", "--playlist"):
            return arg


def main(argv):
    if len(argv) == 0:
        print("pyTraktorPlaylistExporter.py -p <TraktorPlaylist>")
        sys.exit(2)

    playlist = arg_processing(argv)
    TRACK_LIST = parse_collection(playlist)

    print(TRACK_LIST)


if __name__ == '__main__':
    main(sys.argv[1:])


