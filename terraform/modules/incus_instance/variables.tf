variable "name" {
  description = "Unique name for the Incus instance."
  type        = string

  validation {
    condition     = length(trimspace(var.name)) > 0
    error_message = "name must not be empty."
  }
}

variable "project" {
  description = "Incus project that owns the instance."
  type        = string
  default     = "default"
}

variable "image" {
  description = "Explicit Incus image alias or fingerprint supplied by the consumer."
  type        = string

  validation {
    condition     = length(trimspace(var.image)) > 0
    error_message = "image must not be empty."
  }
}

variable "instance_type" {
  description = "Incus instance type."
  type        = string
  default     = "container"

  validation {
    condition     = contains(["container", "virtual-machine"], var.instance_type)
    error_message = "instance_type must be container or virtual-machine."
  }
}

variable "profiles" {
  description = "Incus profiles attached to the instance."
  type        = list(string)
  default     = ["default"]

  validation {
    condition     = length(var.profiles) > 0 && alltrue([for profile in var.profiles : length(trimspace(profile)) > 0])
    error_message = "profiles must contain at least one non-empty profile."
  }
}

variable "ephemeral" {
  description = "Whether Incus removes the instance automatically after it stops."
  type        = bool
  default     = false
}

variable "config" {
  description = "Deployment-neutral Incus instance configuration. Consumers own any environment-specific values."
  type        = map(string)
  default     = {}
}

variable "devices" {
  description = "Optional Incus devices supplied by the consumer."
  type = map(object({
    type       = string
    properties = map(string)
  }))
  default = {}
}
