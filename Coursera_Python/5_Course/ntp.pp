class ntp {
  package { 'ntp':
    ensure => latest,
  }
  file { '/etc/ntp.conf':
    source => '/home/bacuchito/Desktop/Coursera/5_Course/ntp.conf',
    replace => true,
    require => Package['ntp'],
    notify => Service['ntp'], 
  }
  service { 'ntp':
    enable => true,
    ensure => running,
    require => File['/etc/ntp.conf'],
  }
}

include ntp
