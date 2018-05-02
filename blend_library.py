# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Blend Library",
    "author": "Vincent Gires",
    "description": "Asset Manager - Append or link materials/objects/groups/node groups of specific folder locations",
    "version": (0, 3, 2),
    "blender": (2, 7, 4),
    "location": "3D View > Tools || Node Editor > Tools",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Import-Export/Blend_Library",
    "category": "Import-Export"}

import bpy
import os.path

#-------------------------------#
#          CALL BACK            #
#-------------------------------#
def custom_paths_callback_node_groups(self, context):
    bpy.context.scene.node_groups_library_list_compositing.clear()
    bpy.context.scene.node_groups_library_list_shading.clear()
    bpy.context.scene.node_groups_library_list_texture.clear()

def custom_paths_callback_materials(self, context):
    bpy.context.scene.materials_library_list.clear()

def custom_paths_callback_objects(self, context):
    bpy.context.scene.objects_library_list.clear()

def custom_paths_callback_groups(self, context):
    bpy.context.scene.groups_library_list.clear()

#-------------------------------#
#       AddonPreferences        #
#-------------------------------#
class library_addon_preferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    folderpath_nodegroups_compositing = bpy.props.StringProperty(
            name="Compositing Node Groups",
            subtype='DIR_PATH',
            )
    folderpath_nodegroups_shading = bpy.props.StringProperty(
            name="Shading Node Groups",
            subtype='DIR_PATH',
            )
    folderpath_nodegroups_texture = bpy.props.StringProperty(
            name="Texture Node Groups",
            subtype='DIR_PATH',
            )
    folderpath_materials = bpy.props.StringProperty(
            name="Materials",
            subtype='DIR_PATH',
            )
    folderpath_objects = bpy.props.StringProperty(
            name="Objects",
            subtype='DIR_PATH',
            )
    folderpath_groups = bpy.props.StringProperty(
            name="Groups",
            subtype='DIR_PATH',
            )

    list_display_filename = bpy.props.BoolProperty(
        name = "display filename",
        description = "Display the filename in library list",
        default = 1,
    )

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "list_display_filename")

        layout.prop(self, "folderpath_nodegroups_compositing")
        layout.prop(self, "folderpath_nodegroups_shading")
        layout.prop(self, "folderpath_nodegroups_texture")
        layout.prop(self, "folderpath_materials")
        layout.prop(self, "folderpath_objects")
        layout.prop(self, "folderpath_groups")

#-------------------------------#
#          PROPERTIES           #
#-------------------------------#
class blend_library_customPaths_properties(bpy.types.PropertyGroup):

    bpy.types.Scene.customFolderpath_nodegroups_compositing = bpy.props.StringProperty(
        name="Compositing Node Groups",
        subtype='DIR_PATH',
    )
    bpy.types.Scene.customFolderpath_nodegroups_shading = bpy.props.StringProperty(
        name="Shading Node Groups",
        subtype='DIR_PATH',
    )
    bpy.types.Scene.customFolderpath_nodegroups_texture = bpy.props.StringProperty(
        name="Texture Node Groups",
        subtype='DIR_PATH',
    )
    bpy.types.Scene.customFolderpath_materials = bpy.props.StringProperty(
        name="Materials",
        subtype='DIR_PATH',
    )
    bpy.types.Scene.customFolderpath_objects = bpy.props.StringProperty(
        name="Objects",
        subtype='DIR_PATH',
    )
    bpy.types.Scene.customFolderpath_groups = bpy.props.StringProperty(
        name="Groups",
        subtype='DIR_PATH',
    )

class property_node_groups_library_compositing(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="node name", default="Group")
    file = bpy.props.StringProperty(name="file", default="file.blend")

class property_node_groups_library_shading(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="node name", default="Group")
    file = bpy.props.StringProperty(name="file", default="file.blend")

class property_node_groups_library_texture(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="node name", default="Group")
    file = bpy.props.StringProperty(name="file", default="file.blend")

class property_materials_library(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="material name", default="Material")
    file = bpy.props.StringProperty(name="file", default="file.blend")

class property_objects_library(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="object name", default="Object")
    file = bpy.props.StringProperty(name="file", default="file.blend")
    use = bpy.props.BoolProperty(name="use", description="Use this item when importing", default=False)

class property_groups_library(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="group name", default="Group")
    file = bpy.props.StringProperty(name="file", default="file.blend")

class node_groups_library_properties(bpy.types.PropertyGroup):

    bpy.types.Scene.node_groups_library_compositing_index = bpy.props.IntProperty(
        name = "Index",
        default = 0,
        min = 0,
    )

    bpy.types.Scene.node_groups_library_shading_index = bpy.props.IntProperty(
        name = "Index",
        default = 0,
        min = 0,
    )

    bpy.types.Scene.node_groups_library_texture_index = bpy.props.IntProperty(
        name = "Index",
        default = 0,
        min = 0,
    )

    bpy.types.Scene.materials_library_index = bpy.props.IntProperty(
        name = "Index",
        default = 0,
        min = 0,
    )

    bpy.types.Scene.objects_library_index = bpy.props.IntProperty(
        name = "Index",
        default = 0,
        min = 0,
    )

    bpy.types.Scene.groups_library_index = bpy.props.IntProperty(
        name = "Index",
        default = 0,
        min = 0,
    )

    bpy.types.Scene.node_groups_library_addNode = bpy.props.BoolProperty(
        name = "Add node",
        description = "Add node in the node tree",
        default = 1,
    )

    bpy.types.Scene.node_groups_library_single = bpy.props.BoolProperty(
        name = "single-user",
        description = "Append node group only if this group is not in the node groups of the blend file",
        default = 0,
    )

    bpy.types.Scene.materials_library_assign = bpy.props.BoolProperty(
        name = "Assign",
        description = "Assign material to selected object",
        default = 1,
    )

    bpy.types.Scene.materials_library_replace = bpy.props.BoolProperty(
        name = "Replace",
        description = "Replace materials of the selected objects by the imported one",
        default = 0,
    )

    bpy.types.Scene.materials_library_single = bpy.props.BoolProperty(
        name = "single-user",
        description = "Append material only if this material is not in the blend file",
        default = 0,
    )

    bpy.types.Scene.view3d_library_useCursor = bpy.props.BoolProperty(
        name = "Use 3D Cursor",
        default = 0,
    )

    bpy.types.Scene.view3d_library_instanceGroup = bpy.props.BoolProperty(
        name = "Instance Group",
        default = 0,
    )

    bpy.types.Scene.library_customPaths_node_groups = bpy.props.BoolProperty(
        name = "Use custom paths",
        default = 0,
        update = custom_paths_callback_node_groups
    )

    bpy.types.Scene.library_customPaths_materials = bpy.props.BoolProperty(
        name = "Use custom paths",
        default = 0,
        update = custom_paths_callback_materials
    )

    bpy.types.Scene.library_customPaths_objects = bpy.props.BoolProperty(
        name = "Use custom paths",
        default = 0,
        update = custom_paths_callback_objects
    )

    bpy.types.Scene.library_customPaths_groups = bpy.props.BoolProperty(
        name = "Use custom paths",
        default = 0,
        update = custom_paths_callback_groups
    )

    bpy.types.Scene.nodegroups_library_import_type = bpy.props.EnumProperty(
        items = (
            ('append', 'Append', 'Append group to the blend file'),
            ('link', 'Link', 'Link group to the blend file'),
        ),
        name = "Import",
        description = "Append or Link",
        default = 'append',
    )

    bpy.types.Scene.materials_library_import_type = bpy.props.EnumProperty(
        items = (
            ('append', 'Append', 'Append material to the blend file'),
            ('link', 'Link', 'Link material to the blend file'),
        ),
        name = "Import",
        description = "Append or Link",
        default = 'append',
    )

    bpy.types.Scene.objects_library_import_type = bpy.props.EnumProperty(
        items = (
            ('append', 'Append', 'Append object to the blend file'),
            ('link', 'Link', 'Link object to the blend file'),
        ),
        name = "Import",
        description = "Append or Link",
        default = 'append',
    )

    bpy.types.Scene.groups_library_import_type = bpy.props.EnumProperty(
        items = (
            ('append', 'Append', 'Append group to the blend file'),
            ('link', 'Link', 'Link group to the blend file'),
        ),
        name = "Import",
        description = "Append or Link",
        default = 'append',
    )

#-------------------------------#
#          FUNCTIONS            #
#-------------------------------#
def get_addon_preferences():
    #addon_preferences = bpy.context.user_preferences.addons['blend_library'].preferences # file name
    addon_preferences = bpy.context.user_preferences.addons[__name__].preferences
    return addon_preferences

def import_from_library(datablock, folderpath, file, selected, link, instance_group=False):

    folderpath = bpy.path.abspath(folderpath)

    if link:
        bpy.ops.wm.link(directory=folderpath+"//"+file+"/"+datablock+"/", filepath=file, filename=selected)

    else:
        bpy.ops.wm.append(directory=folderpath+"//"+file+"/"+datablock+"/", filepath=file, filename=selected, instance_groups=instance_group)

def scan_folder_nodes(folderpath, tree_type):

    folderpath = bpy.path.abspath(folderpath)

    for file in os.listdir(folderpath):
        if file.endswith(".blend"):

            filepath = folderpath+"\\"+file

            # look node_groups through file
            with bpy.data.libraries.load(filepath) as (data_from, data_to):

                for name in data_from.node_groups:

                    # add node_groups to list
                    if tree_type == "compositing":
                        my_item = bpy.context.scene.node_groups_library_list_compositing.add()
                    elif tree_type == "shading":
                        my_item = bpy.context.scene.node_groups_library_list_shading.add()
                    elif tree_type == "texture":
                        my_item = bpy.context.scene.node_groups_library_list_texture.add()
                    my_item.name = name
                    my_item.file = file
