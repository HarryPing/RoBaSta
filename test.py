import os
from win32com.client import Dispatch


SRC = r"F:\tmp"
DST = r"F:\tmp2"

shell = Dispatch("Shell.Application")

# Hilfsfunktion, um das Property-Index für "Rating" zu finden
def find_rating_index(folder):
    for i in range(0, 50):
        # print(folder.Items().item(0))
        name = folder.GetDetailsOf(folder.Items().Item(0), i)
        # print(name, i)
        print(folder.GetDetailsOf(folder.Items().Item(0), 19))
        if "Stern" in name:
            return i
    raise RuntimeError("Index für Rating nicht gefunden")

def copy_ratings(src_root, dst_root):
    for root, dirs, files in os.walk(src_root):
        rel = os.path.relpath(root, src_root)
        dst_dir = os.path.join(dst_root, rel)
        src_ns = shell.NameSpace(root)
        dst_ns = shell.NameSpace(dst_dir)
        idx = find_rating_index(src_ns)

        # Verzeichnisse im Ziel anlegen
        for d in dirs:
            target = os.path.join(dst_dir, d)
            if not os.path.exists(target):
                os.makedirs(target)

        for f in files:
            src_item = src_ns.ParseName(f)
            dst_item = dst_ns.ParseName(f)
            if not dst_item:
                continue
            rating = src_ns.GetDetailsOf(src_item, idx)
            if rating:
                dst_ns.SetDetailsOf(dst_item, idx, rating)

copy_ratings(SRC, DST)
print("Fertig! Bewertungen übertragen.")
