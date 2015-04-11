#!/usr/bin/env python
import typecheck_pb2

point = typecheck_pb2.Point(x=1.5, y=2.75)
assert point.IsInitialized()

point = typecheck_pb2.Point(x=1.5)
assert not point.IsInitialized()

try:
  point = typecheck_pb2.Point(x=1.2, y="asdf")
  assert False
except TypeError, e:
  pass

place = typecheck_pb2.Place(name="wtanaka.com",
    location=typecheck_pb2.Point(x=1.5, y=2.75))
assert place.IsInitialized()

place = typecheck_pb2.Place(name="wtanaka.com",
    location=typecheck_pb2.Point(x=1.5, y=2.75),
        review=typecheck_pb2.Review(rating=4,
        text="4 stars would come again"))
assert place.IsInitialized()

try:
  place = typecheck_pb2.Place(name="wtanaka.com",
      location=typecheck_pb2.Point(x=1.5, y=2.75),
          review=typecheck_pb2.Point(x=1.5, y=2.75))
  assert False
except TypeError, e:
  pass
