from app import App
from movementsystem import SimplePositioningDataBase

if __name__ == "__main__":
    world_map = SimplePositioningDataBase()
    app = App(world_map)
    app.mainloop()
