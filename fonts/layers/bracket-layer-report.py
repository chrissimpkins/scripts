# Copyright 2020 Christopher Simpkins

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import GlyphsApp  # noqa: F401

font = Glyphs.font  # noqa: F821
try:
    for this_glyph in font.glyphs:
        for layer in this_glyph.layers:
            if "[" in layer.name:
                print("{} {}".format(this_glyph.name, layer.name))
except TypeError as e:
    print("ERROR: {}. {}".format(e, this_glyph.name))
