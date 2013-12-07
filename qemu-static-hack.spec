Summary:        Hack for ARM ABF builder
Name:           qemu-static-hack
Version:        1.4.0
Release:        5
License:        GPLv2+
Group:          Monitoring
Url:            https://abf.rosalinux.ru
Source0:        qemu-static-arm
Source1:        qemu-static-arm-binfmt
Source2:        qemu-wrapper
Source3:	qemu-wrapper.c
BuildArch:	noarch


%description
Qemu static package to trick mock-urpm builder

%prep
echo "Empty prep section"

%build
echo "Empty install section"

%install
mkdir -p %{buildroot}/%{_bindir}/
install -D -m 0755 %{SOURCE0} %{buildroot}/%{_bindir}/
install -D -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}/
install -D -m 0755 %{SOURCE2} %{buildroot}/%{_bindir}/

%files
%{_bindir}/qemu*
