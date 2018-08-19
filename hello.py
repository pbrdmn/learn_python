def world(msg):
  return msg


def world_capitalize(msg):
  return msg.capitalize()


def world_split(msg):
  return msg.split()


if __name__ == '__main__':
    msg = "Hello, World!"
    print(world(msg))
    print(world_capitalize(msg))
    print(world_split(msg))
