import defusedxml
import getopt
import sys


TRACK_LIST = []


def parse_collection(playlist):
    collection = r"C:\Users\Thomas.defise\Documents\Native Instruments\Traktor 2.11.3\collection.nml"

    defusedxml.defuse_stdlib()
    tree = defusedxml.ElementTree.parse(collection)
    track_list = list()
	
    for a in tree.iter(tag="NODE"):
        if a.get("NAME") == playlist:
            for z in a.iter(tag="PRIMARYKEY"):
                windows_path_track = z.get("KEY").replace("/:", "\\")
                track_list.append(windows_path_track)

    return track_list


def arg_processing(argv):

    if not argv:
        print("pyTraktorPlaylistExporter.py -p <TraktorPlaylist>")
        sys.exit(2)

    try:
        opts, _ = getopt.getopt(argv, "hp:", ["playlist="])
    except getopt.GetoptError:
        print("pyTraktorPlaylistExporter.py -p <TraktorPlaylist>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit(2)
        elif opt in ("-p", "--playlist"):
            return arg


def main(argv):

    playlist = arg_processing(argv)
    track_list = parse_collection(playlist)

    print(track_list)


if __name__ == '__main__':
    main(sys.argv[1:])
