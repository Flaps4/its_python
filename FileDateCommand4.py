import sys,os,shutil,datetime,argparse

parser = argparse.ArgumentParser(description='Skriv ut filex med speciellt path och extenstion')
parser.add_argument("-d", required=True, type=str, help="Path to files")
parser.add_argument("-f", required=True, type=str, help="file extemsion")
args = parser.parse_args()

filer = []

for root, dirs, files in os.walk(args.d):
    for file in files:
        if file.endswith(f".{args.f}"):
             #print(os.path.join(root, file))
             filer.append(os.path.join(root, file))

print("--------------------------------------------------------------------------------")


for files in filer:

    print(f"Fil: {files}" , f"Storlek på denna fil är: {os.path.getsize(files)} bytes")
