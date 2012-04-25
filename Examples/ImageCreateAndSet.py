#=========================================================================
#
#  Copyright Insight Software Consortium
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#=========================================================================
#!/usr/bin/env python

import SimpleITK as sitk

xImg = sitk.Image( 256, 256, sitk.sitkFloat32 )
yImg = sitk.Image( 256, 256, sitk.sitkFloat32 )

for y in range( 0, xImg.GetSize()[1] ):
    for x in range( 0, xImg.GetSize()[0] ):
        xImg.SetPixel( x, y, x )
        yImg[x, y] = y


sigma = 50

xImg = sitk.SubtractConstantFrom( xImg,  xImg.GetSize()[0] / 2 )
yImg = yImg - yImg.GetSize()[1] / 2

gaussianImg = sitk.Exp( -1 * (xImg*xImg + yImg*yImg) / (2.0 * sigma**2) )

# sitk.Show( gaussianImg )