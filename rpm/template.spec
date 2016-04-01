Name:           ros-indigo-cob-description
Version:        0.6.5
Release:        0%{?dist}
Summary:        ROS cob_description package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosunit
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin

%description
This package contains the description (mechanical, kinematic, visual, etc.) of
the Care-O-bot robot. The files in this package are parsed and used by a variety
of other components. Most users will not interact directly with this package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Apr 01 2016 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Sat Aug 29 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Mon Dec 15 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Wed Sep 24 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Tue Sep 16 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Wed Aug 27 2014 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.5.5-0
- Autogenerated by Bloom

