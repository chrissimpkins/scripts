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

PRE_BRACKET_SIZE = "16"
POST_BRACKET_SIZE = "18"

font = Glyphs.font  # noqa: F821
try:
    for this_glyph in font.glyphs:
        for layer in this_glyph.layers:
            # test for bracket layer opening delimiter
            # identifier and the expected pre value
            if "[" in layer.name and PRE_BRACKET_SIZE in layer.name:
                # edit to the desired post value
                layer.name = layer.name.replace(PRE_BRACKET_SIZE, POST_BRACKET_SIZE)
                print(
                    "{} in {} updated to {}".format(
                        this_glyph.name, layer.master, POST_BRACKET_SIZE
                    )
                )
except TypeError as e:
    print("ERROR: {}. {}".format(e, this_glyph.name))

font.save()
