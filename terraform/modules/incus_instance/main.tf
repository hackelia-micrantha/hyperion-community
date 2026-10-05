resource "incus_instance" "this" {
  name      = var.name
  project   = var.project
  image     = var.image
  type      = var.instance_type
  profiles  = var.profiles
  config    = var.config
  ephemeral = var.ephemeral

  dynamic "device" {
    for_each = var.devices
    content {
      name       = device.value.name
      type       = device.value.type
      properties = device.value.properties
    }
  }
}
