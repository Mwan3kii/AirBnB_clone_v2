# Redo the task #0 but by using Puppet
exec { 'update_server':
  command => '/usr/bin/env apt-get -y update',
}
-> exec {'install_nginx':
  command => '/usr/bin/env apt-get -y install nginx',
}
-> exec {'creates_release_test':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'creates_folder_shared':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec {'write_index_html':
  command => '/usr/bin/env echo "Hello Wolrd Puppet" | sudo tee /data/web_static/releases/test/index.html',
}
-> exec {'create_symbolic_link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
-> exec {'set_ownership':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
-> exec {'update_nginx_config':
  command => '/usr/bin/env sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> exec {'restart_nginx':
  command => '/usr/bin/env service nginx restart',
}
